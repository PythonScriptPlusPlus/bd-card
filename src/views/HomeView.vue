<template>
  <div class="home">
    <ParallaxHeader id="my-canvas"/>
    <statistics-component />
    <wishes-component />
  </div>
</template>

<script>
// @ is an alias to /src
import ParallaxHeader from '@/components/ParallaxHeader.vue';
import StatisticsComponent from '@/components/StatisticsComponent.vue';
import WishesComponent from '@/components/WishesComponent.vue';

export default {
  name: 'HomeView',
  components: {
    ParallaxHeader,
    StatisticsComponent,
    WishesComponent,
  },
};

</script>
