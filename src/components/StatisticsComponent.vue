<template>
    <div class="statistics__header">
        <h1 class="statistics__title">Год был невероятным</h1>
        <h2 class="statistics__subtitle">А твой телеграм был хорошим способом запечатлеть это!</h2>
        <div class="elements-list" role="list">
            <div class="element" v-for="(fact, index) in facts" :key="index" role="listitem">
                <div class="element__wrapper">
                  <div>
                    <h3 class="element__title">{{ fact.title }}</h3>
                    <p class="element__subtitle">{{ fact.subtitle }}</p>
                  </div>
                  <div class="element__bottom">
                    <img
                      v-if="fact.image"
                      class="element__image"
                      :src="fact.image"
                      :alt="fact.title || ''"
                      loading="lazy"
                    />
                  </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      facts: [
        {
          title: '127 постов сделано за этот год!',
          subtitle: 'Весь СММ Billie Eilish смог себе позволить только 64 поста в инстаграме за тот же период',
          image: '/img/stats/post_counts.png',
        },
        {
          title: 'Твои посты настолько вовлекающие, что суммарно они получили 1701 реакцию',
          subtitle: 'из них 1031 ❤️',
          image: '/img/stats/hearts_vs.png',
        },
        {
          title: 'Пост с наибольшим количеством реакций',
          subtitle: '',
          image: '/img/stats/summer_review.png',
        },
        {
          title: 'Единственный пост с негативными реакциями - о сентябре',
          subtitle: 'Очень даже понимаемо!',
          image: '/img/stats/September.jpg',
        },
        {
          title: 'Постов с фото',
          subtitle: '87 постов, в которых 495 фото',
        },
        {
          title: 'Постов с видео',
          subtitle: '57 постов, в которых 152 видео',
        },
        {
          title: 'Среднее количество просмотров на пост',
          subtitle: '115 просмотров',
        },
        {
          title: 'Самый просматриваемый пост',
          subtitle: 'очень неожиданный ответ на 558 просмотров',
          image: '/img/stats/most_viewed.png',
        },
        {
          title: 'Суммарные просмотры',
          subtitle: '15524 просмотра',
        },
        {
          title: 'Самый активный месяц',
          subtitle: 'сентябрь 2025 — 19 постов',
        },
        {
          title: 'Больше всего постов по дням недели',
          subtitle: 'пятница — 26 постов',
        },
        {
          title: 'Самый длинный перерыв между постами - c 29 июля по 15 августа',
          subtitle: 'где ты была?',
        },
        {
          title: 'Самое употребляемое слово (не предлог/местоимение)',
          subtitle: '«люблю»',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.statistics {

    &__title {
        font-size: 3em;
        margin: 0;
    }

    &__subtitle {
        font-size: 1.5em;
        padding-bottom: 20px;
        margin: 0;
        border-bottom: 2px solid #2c3e50;
    }

    &__header {
        min-height: 100vh;
        padding-top: 5%;
        margin: 20px;
    }
}

.element {
  // flex: 0 0 80%;
  min-width: 260px;  /* ensures usable width on small screens */
  max-width: 600px;
  scroll-snap-align: center;
  background: transparent;
  box-sizing: border-box;

  &__image {
    width: 95%;
    height: auto;
    // aspect-ratio: 1/2;
  }

  &__wrapper {
    display: flex;
    flex-direction: column;
    height: calc(2/3 * 100vh);
    aspect-ratio: 2/5;
    margin-bottom: 0;
    text-align: left;
    padding: 16px;
    border-radius: 8px;
    /* optional card visuals */
    background: rgba(255,255,255,0.03);
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  }

  &__title {
    margin: 0;
  }

  &__subtitle {
    margin: 0;
  }

  &__bottom {
    flex: 1 1 auto;             /* take remaining vertical space */
    display: flex;
    align-items: center;        /* vertical centering inside middle area */
    justify-content: center;    /* horizontal centering */
    padding: 8px 0;
  }
}

/* horizontal scroll list */
.elements-list {
    display: flex;
    gap: 18px;
    padding: 20px 10px;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch; /* smooth touch scrolling on iOS */
    scroll-snap-type: x mandatory;
    align-items: start;
}

/* optional: hide native scrollbar for a cleaner look (still scrollable) */
.elements-list::-webkit-scrollbar {
  height: 8px;
}
.elements-list::-webkit-scrollbar-thumb {
  background: rgba(0,0,0,0.2);
  border-radius: 6px;
}
</style>
