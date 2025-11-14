<!-- eslint-disable vuejs-accessibility/media-has-caption -->
<!-- eslint-disable vuejs-accessibility/media-has-caption -->
<template>
    <div>
        <video
            id="video"
            ref="video"
            controls
            preload="metadata"
            autoplay
            loop
            muted
            playsinline
        >
            <source src="/img/mermaid.mp4" type="video/mp4" />
        </video>
    </div>
</template>

<script>
export default {
  mounted() {
    const vid = this.$refs.video;
    if (vid && typeof vid.play === 'function') {
      vid.play().catch(() => {
        // Autoplay blocked by browser; user interaction required
      });
    }
  },
};
</script>

<style lang="scss" scoped>
#video {
    width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
}
</style>
