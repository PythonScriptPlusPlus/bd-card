<template>
  <div
    class="parallax"
    :style="{ '--parallax-bg-pos-y': `${150 - offset}px` }"
  >
    <canvas ref="confettiCanvas" width="100%" height="100%"></canvas>
    <h1 class="parallax__title">Happy Birthday!</h1>
    <p>серьёзной дате - серьёзное поздравление</p>
  </div>
</template>

<script>
// eslint-disable-next-line import/no-extraneous-dependencies
import confetti from 'canvas-confetti';

export default {
  name: 'ParallaxHeader',
  data() {
    return {
      offset: 0,
    };
  },
  mounted() {
    // Create a canvas element and append it to the body
    const canvas = this.$refs.confettiCanvas;
    canvas.style.position = 'absolute';
    canvas.style.pointerEvents = 'none';
    canvas.style.top = 0;
    canvas.style.left = 0;
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.zIndex = 2;

    // Initialize confetti only once
    const myConfetti = confetti.create(canvas, { resize: true });

    // Fire confetti bursts
    const count = 200;
    const defaults = {
      origin: { y: 0.7 },
    };

    function fire(particleRatio, opts) {
      myConfetti({
        ...defaults,
        ...opts,
        particleCount: Math.floor(count * particleRatio),
      });
    }

    fire(0.25, {
      spread: 26,
      startVelocity: 55,
    });
    fire(0.2, {
      spread: 60,
    });
    fire(0.35, {
      spread: 100,
      decay: 0.91,
      scalar: 0.8,
    });
    fire(0.1, {
      spread: 120,
      startVelocity: 25,
      decay: 0.92,
      scalar: 1.2,
    });
    fire(0.1, {
      spread: 120,
      startVelocity: 45,
    });

    // Add scroll event listener
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeUnmount() {
    // Clean up the canvas when the component is destroyed
    const canvas = document.getElementById('my-canvas');
    if (canvas) {
      canvas.remove();
    }
    // Remove scroll event listener
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.offset = window.pageYOffset * 1.5; // Adjust multiplier for speed
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.parallax {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;

  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('../../public/img/collage_output.png');
    background-attachment: fixed;
    background-position-x: center;
    background-position-y: var(--parallax-bg-pos-y, 50px);
    background-repeat: repeat;
    background-size: cover;
    filter: blur(2px);
    z-index: 1;
  }

  > * {
    position: relative;
    z-index: 2;
  }

  &__title {
    padding-top: 40vh;
    margin: 0;
    font-size: 3em;
    color: #333;
  }

  // will-change: transform;
  // transition: transform 0.1s linear;
}
</style>
