<!-- eslint-disable vuejs-accessibility/media-has-caption -->
<template>
  <div class="vas-component">
    <div class="photo"></div>
    <!-- show visible player; keep autoplay if you want it to start muted -->
    <audio controls loop playsinline>
      <source src="/img/BURNOUT.mp3" type="audio/mpeg" />
      Your browser does not support the audio element.
    </audio>
  </div>
</template>

<script>
export default {
};
</script>

<style lang="scss" scoped>
.photo {
    width: 100%;
    aspect-ratio: 1/1.34;
    background-image: url('../../../public/img/vas.jpg');
    background-repeat: no-repeat;
    background-size: cover;
}

</style>
