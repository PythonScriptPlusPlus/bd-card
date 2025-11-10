<template>
    <div>
        <h1>Пожелания</h1>
        <h2>От друзей и близких</h2>
        <div class="wishes">
            <div v-for="wish in wishes" :key="wish.from" class="wishes__wrapper">
                <h3 class="wishes__from">От: {{ wish.from }}</h3>
                <p class="wishes__message">{{ wish.message }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      wishes: [
        {
          from: 'Alice',
          message: 'Happy Birthday! Wishing you a day filled with love and joy.',
        },
        {
          from: 'Bob',
          message: 'May your birthday be as special as you are!',
        },
        {
          from: 'Charlie',
          message: 'Cheers to another year of amazing adventures!',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>

</style>
