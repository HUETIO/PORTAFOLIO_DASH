import time
import random
import pytest
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    TimeoutException
)
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://localhost:5173/"
ARTIFACTS_DIR = Path(__file__).parent / "artifacts" / "screenshots"

# ------------------------
# HOOKS / QA TELEMETRY
# ------------------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# ------------------------
# UTILIDADES
# ------------------------

def human_pause(min_s=0.2, max_s=0.8):
    time.sleep(random.uniform(min_s, max_s))

def safe_click(driver, element):
    try:
        element.click()
    except (ElementClickInterceptedException, StaleElementReferenceException):
        driver.execute_script("arguments[0].click();", element)

@pytest.fixture(autouse=True)
def qa_test_telemetry(request):
    started_at = time.perf_counter()
    yield
    duration = time.perf_counter() - started_at
    print(f"\n[QA] {request.node.name} -> {duration:.2f}s")

    rep_call = getattr(request.node, "rep_call", None)
    if not rep_call or rep_call.passed:
        return

    driver_obj = request.node.funcargs.get("driver")
    if not driver_obj:
        return

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = request.node.name.replace(" ", "_")
    screenshot = ARTIFACTS_DIR / f"{safe_name}_{ts}.png"
    driver_obj.save_screenshot(str(screenshot))
    print(f"[QA] Screenshot por fallo: {screenshot}")

# ------------------------
# FIXTURE DRIVER
# ------------------------

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")

    service = ChromeService(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    try:
        drv.maximize_window()
    except Exception:
        pass
    drv.implicitly_wait(2)
    yield drv
    drv.quit()

# ------------------------
# TEST 1: ACCESO PÚBLICO SIN LOGIN
# ------------------------

@pytest.mark.regression
def test_public_access_without_login(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    assert not driver.find_elements(By.CSS_SELECTOR, ".auth-btn")
    assert not driver.find_elements(By.CSS_SELECTOR, "input[type='password']")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title-stack")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".projects-section")))
    wait.until(EC.element_to_be_clickable((By.ID, "morph-btn"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".agent-modal")))

# ------------------------
# TEST 3: STRESS MODALES DE PELÍCULAS
# ------------------------

@pytest.mark.stress
def test_stress_movie_modals(driver):
    wait = WebDriverWait(driver, 10)

    cinema_section = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#cinema-container"))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        cinema_section
    )

    CYCLES = 5
    print(f"\n[Stress] Modales de películas x{CYCLES}")

    for i in range(CYCLES):
        cards = driver.find_elements(By.CSS_SELECTOR, ".movie-card")
        if not cards:
            pytest.fail("No se cargaron películas")

        card = cards[i % len(cards)]

        ActionChains(driver).move_to_element(card).perform()
        human_pause(0.2, 0.5)

        play_btn = card.find_element(By.CSS_SELECTOR, ".btn-play")
        driver.execute_script("arguments[0].click();", play_btn)

        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-window"))
        )

        human_pause(0.3, 0.8)

        close_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-actions button"))
        )
        close_btn.click()

        wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-window"))
        )

    print("✅ Stress modales OK")

# ------------------------
# TEST 4: STRESS TABS RÁPIDOS
# ------------------------

@pytest.mark.stress
def test_stress_rapid_tabs(driver):
    wait = WebDriverWait(driver, 5)

    tabs_section = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".color-buttons"))
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        tabs_section
    )

    buttons = driver.find_elements(By.CSS_SELECTOR, ".color-buttons button")
    assert buttons, "No hay botones de tabs"

    CYCLES = 5
    print(f"\n[Stress] Tabs rápidos x{CYCLES}")

    for i in range(CYCLES):
        btn = buttons[i % len(buttons)]
        btn.click()

        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tabs-container"))
        )

        human_pause(0.1, 0.4)

        if i % 5 == 0:
            try:
                close_tab = driver.find_element(By.CSS_SELECTOR, ".close-tab")
                if close_tab.is_displayed():
                    close_tab.click()
            except Exception:
                pass

    print("✅ Stress tabs OK")

# ------------------------
# TEST 5: SMOKE SECCIONES PRINCIPALES
# ------------------------

@pytest.mark.smoke
def test_smoke_main_sections(driver):
    wait = WebDriverWait(driver, 8)
    driver.get(BASE_URL)

    hero = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.hero")))
    assert hero.is_displayed(), "No se visualiza el hero principal"

    cinema = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cinema-container")))
    assert cinema.is_displayed(), "No se visualiza la sección Cinema Explorer"

    tabs = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".color-buttons")))
    assert tabs.is_displayed(), "No se visualiza la sección de tabs de color"

    print("✅ Smoke de secciones principales OK")

# ------------------------
# TEST 6: NAVEGACIÓN INTERNA DEL MODAL (SIGUIENTE)
# ------------------------

@pytest.mark.regression
def test_movie_modal_next_navigation(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    cinema_section = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#cinema-container"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", cinema_section)

    first_card = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".movie-card")))
    ActionChains(driver).move_to_element(first_card).perform()
    human_pause(0.2, 0.4)

    play_btn = first_card.find_element(By.CSS_SELECTOR, ".btn-play")
    safe_click(driver, play_btn)

    modal_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-window h2")))
    before_title = modal_title.text.strip()

    next_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-actions button:last-child"))
    )

    if next_btn.is_enabled():
        safe_click(driver, next_btn)
        wait.until(lambda d: d.find_element(By.CSS_SELECTOR, ".modal-window h2").text.strip() != before_title)

    close_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-actions button:first-child")))
    safe_click(driver, close_btn)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-window")))

    print("✅ Navegación dentro de modal OK")

# ------------------------
# TEST 7: ENLACES DE CONTACTO (INTEGRIDAD)
# ------------------------

@pytest.mark.smoke
def test_contact_links_integrity(driver):
    wait = WebDriverWait(driver, 8)
    driver.get(BASE_URL)

    contact_heading = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(., 'Conecta Conmigo')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", contact_heading)

    links = driver.find_elements(By.CSS_SELECTOR, ".contact-links a")
    assert len(links) >= 4, "Se esperaban al menos 4 enlaces de contacto"

    for link in links:
        href = (link.get_attribute("href") or "").strip()
        assert href, "Se encontró un enlace sin href"
        parsed = urlparse(href)
        assert parsed.scheme in {"http", "https", "mailto"}, f"Esquema no válido en enlace: {href}"

    print("✅ Integridad de enlaces de contacto OK")

# ------------------------
# TEST 8: MENÚ MÓVIL (TOGGLE)
# ------------------------

@pytest.mark.regression
def test_mobile_menu_toggle(driver):
    wait = WebDriverWait(driver, 8)
    driver.set_window_size(390, 844)
    driver.get(BASE_URL)

    toggle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-toggle")))
    safe_click(driver, toggle)

    menu = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-menu")))
    menu_classes = menu.get_attribute("class") or ""
    assert "active" in menu_classes, "El menú móvil no se activó al abrir"

    safe_click(driver, toggle)
    wait.until(lambda d: "active" not in ((d.find_element(By.CSS_SELECTOR, ".nav-menu").get_attribute("class") or "")))

    # Restaurar tamaño desktop para no afectar otros tests manuales posteriores.
    driver.set_window_size(1920, 1080)
    print("✅ Toggle de menú móvil OK")
