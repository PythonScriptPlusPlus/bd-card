<template>
    <div>
        <h1 class="wishes__title">Пожелания</h1>
        <h2 class="wishes__subtitle">От друзей и близких</h2>
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
.wishes {
  padding: 20px;

  &__title {
    font-size: 2rem;
    margin-bottom: 0;
  }

  &__subtitle {
    font-size: 1.5rem;
    margin: 0;
  }

  &__wrapper {
    text-align: left;
    padding: 10px;
    margin-bottom: 30px;

    &:nth-of-type(even) {
      text-align: right;
      background-color: #f9f9f9;
    }
  }

  &__from {
    font-weight: bold;
    margin: 0;
  }
  &__message {
    font-size: 1.2rem;
    margin: 0;
  }
}
</style>
