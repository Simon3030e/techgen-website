/**
 * noktostudio — canvas-hero.js
 * Animated network graph: floating nodes + connecting lines
 */

(function () {
  const canvas = document.getElementById('hero-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let W, H, nodes, animId;

  const CONFIG = {
    nodeCount:       65,
    nodeRadius:      2.5,
    nodeColor:       'rgba(108, 99, 255, ',   // opacity appended
    lineColor:       'rgba(140, 133, 255, ',  // opacity appended
    maxDist:         160,
    speed:           0.35,
    mouseRadius:     180,
    mousePush:       0.04,
  };

  // Track mouse for subtle interactivity
  const mouse = { x: -9999, y: -9999 };
  canvas.addEventListener('mousemove', e => {
    const r = canvas.getBoundingClientRect();
    mouse.x = e.clientX - r.left;
    mouse.y = e.clientY - r.top;
  });
  canvas.addEventListener('mouseleave', () => { mouse.x = -9999; mouse.y = -9999; });

  function resize() {
    W = canvas.width  = canvas.offsetWidth;
    H = canvas.height = canvas.offsetHeight;
  }

  function createNode() {
    const angle = Math.random() * Math.PI * 2;
    const speed = (0.3 + Math.random() * CONFIG.speed);
    return {
      x:   Math.random() * W,
      y:   Math.random() * H,
      vx:  Math.cos(angle) * speed,
      vy:  Math.sin(angle) * speed,
      r:   CONFIG.nodeRadius * (0.7 + Math.random() * 0.6),
      opacity: 0.35 + Math.random() * 0.45,
    };
  }

  function init() {
    resize();
    nodes = Array.from({ length: CONFIG.nodeCount }, createNode);
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);

    // Draw connecting lines
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dx = nodes[i].x - nodes[j].x;
        const dy = nodes[i].y - nodes[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < CONFIG.maxDist) {
          const alpha = (1 - dist / CONFIG.maxDist) * 0.25;
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.strokeStyle = CONFIG.lineColor + alpha + ')';
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      }
    }

    // Draw nodes
    for (const n of nodes) {
      ctx.beginPath();
      ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
      ctx.fillStyle = CONFIG.nodeColor + n.opacity + ')';
      ctx.fill();
    }
  }

  function update() {
    for (const n of nodes) {
      // Mouse repulsion
      const mdx = n.x - mouse.x;
      const mdy = n.y - mouse.y;
      const md  = Math.sqrt(mdx * mdx + mdy * mdy);
      if (md < CONFIG.mouseRadius && md > 0) {
        const force = (1 - md / CONFIG.mouseRadius) * CONFIG.mousePush;
        n.vx += (mdx / md) * force;
        n.vy += (mdy / md) * force;
      }

      // Dampen velocity
      n.vx *= 0.995;
      n.vy *= 0.995;

      // Move
      n.x += n.vx;
      n.y += n.vy;

      // Bounce off edges
      if (n.x < 0)  { n.x = 0;  n.vx *= -1; }
      if (n.x > W)  { n.x = W;  n.vx *= -1; }
      if (n.y < 0)  { n.y = 0;  n.vy *= -1; }
      if (n.y > H)  { n.y = H;  n.vy *= -1; }
    }
  }

  function loop() {
    update();
    draw();
    animId = requestAnimationFrame(loop);
  }

  window.addEventListener('resize', () => {
    cancelAnimationFrame(animId);
    resize();
    loop();
  });

  init();
  loop();
})();
