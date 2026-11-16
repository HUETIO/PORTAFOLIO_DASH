import time
import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://localhost:5173/"

# ------------------------
# UTILIDADES
# ------------------------

def human_pause(min_s=0.2, max_s=0.8):
    time.sleep(random.uniform(min_s, max_s))

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
