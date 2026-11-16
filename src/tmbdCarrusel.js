// src/lib/btnAnimation.js
export function animateShape(node) {
    const shape = node.querySelector("#btn-shape");
    const text = node.querySelector('.btn-text');
    if (!shape || !text) return;

    let t = 0;
    const colors = ["#00ffd5", "#2196f3", "#4caf50", "#ff4081", "#ff9800", "#b626ff"];

    function lerpColor(c1, c2, t) {
        const r1 = parseInt(c1.slice(1, 3), 16), g1 = parseInt(c1.slice(3, 5), 16), b1 = parseInt(c1.slice(5, 7), 16);
        const r2 = parseInt(c2.slice(1, 3), 16), g2 = parseInt(c2.slice(3, 5), 16), b2 = parseInt(c2.slice(5, 7), 16);
        const r = Math.round(r1 + t * (r2 - r1)), g = Math.round(g1 + t * (g2 - g1)), b = Math.round(b1 + t * (b2 - b1));
        return `#${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16).padStart(2, '0')}`;
    }

    shape.setAttribute("stroke-width", "1.5");
    shape.setAttribute("stroke-opacity", "0.4");

    let frameId;
    function frame() {
        t += 0.03;
        const wave = Math.sin(t) * 8 + Math.sin(t * 1.3) * 4;
        const curve = Math.cos(t * 0.7) * 18 + Math.sin(t * 0.5) * 6;

        const d = `M0,0 Q50,${20 + wave} 100,0 Q${60 + Math.sin(t * 0.4) * 10},${45 + curve} 0,0 Z`;
        shape.setAttribute("d", d);

        const colorSpeed = 0.05;
        const progress = (t * colorSpeed) % 1;
        const colorIndex = Math.floor(t * colorSpeed) % colors.length;
        const nextIndex = (colorIndex + 1) % colors.length;
        const currentColor = lerpColor(colors[colorIndex], colors[nextIndex], progress);

        const r = parseInt(currentColor.slice(1, 3), 16), g = parseInt(currentColor.slice(3, 5), 16), b = parseInt(currentColor.slice(5, 7), 16);
        const oppR = 255 - r, oppG = 255 - g, oppB = 255 - b;

        node.style.background = `linear-gradient(135deg, ${currentColor} 0%, rgba(${r},${g},${b},0.8) 40%, rgba(${oppR},${oppG},${oppB},0.3) 70%, rgb(${oppR},${oppG},${oppB}) 100%)`;
        node.style.backgroundSize = "200% 200%";
        node.style.backgroundPosition = `${(progress * 100)}% 0`;

        const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
        text.style.color = luminance > 0.5 ? "#000" : "#fff";
        
        shape.setAttribute("stroke", currentColor);
        shape.setAttribute("fill", currentColor);

        frameId = requestAnimationFrame(frame);
    }

    frame();

    return {
        destroy() {
            cancelAnimationFrame(frameId);
        }
    };
}