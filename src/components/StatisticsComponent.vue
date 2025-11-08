<template>
    <div class="statistics__header">
        <h1 class="statistics__title">Год был невероятным</h1>
        <h2 class="statistics__subtitle">А твой телеграм был хорошим способом запечатлеть это!</h2>

        <!-- horizontal scroll container -->
        <div class="elements-list" role="list">
            <div class="elements__item" v-for="(fact, index) in facts" :key="index" role="listitem">
                <div class="elements__wrapper">
                    <h3 class="elements__title">{{ fact.title }}</h3>
                    <p class="elements__subtitle">{{ fact.subtitle }}</p>
                    <div
                        class="elements__image"
                        :style="fact.image ? { backgroundImage: `url(${fact.image})` } : null"
                    ></div>
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
          subtitle: 'Это как у Карла Лагерфелда, но на 127 больше',
        },
        {
          title: 'Твои посты настолько вовлекающие, что суммарно они получили 1701 реакцию',
          subtitle: 'из них 1031 ❤️',
        },
        {
          title: 'Среднее число реакций на пост',
          subtitle: '13.3 реакции в среднем',
        },
        {
          title: 'Наиболее реактивные посты',
          subtitle: 'sss',
        },
        {
          title: 'Единственный пост с негативными реакциями',
          subtitle: 'о начале сентября',
        },
        {
          title: 'Постов с фото',
          subtitle: '87 постов',
        },
        {
          title: 'Всего фото',
          subtitle: '495 фото',
        },
        {
          title: 'Процент сообщений с фото',
          subtitle: '68.50%',
        },
        {
          title: 'Постов с видео',
          subtitle: '57 постов',
        },
        {
          title: 'Всего видео',
          subtitle: '152 видео',
        },
        {
          title: 'Процент сообщений с видео',
          subtitle: '44.88%',
        },
        {
          title: 'Самый просматриваемый пост',
          subtitle: 'подготовка к видео про окончание колледжа',
        },
        {
          title: 'Среднее количество просмотров на пост',
          subtitle: '115 просмотров',
        },
        {
          title: 'Суммарные просмотры',
          subtitle: '15524 просмотра',
        },
        {
          title: 'Пересланные посты',
          subtitle: '14 постов были пересланы от других',
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
          title: 'Самый длинный перерыв между постами',
          subtitle: 'между 29 июля и 15 августа',
        },
        {
          title: 'Самый длинный пост',
          subtitle: '234 слова (23.12.2024)',
        },
        {
          title: 'Самое употребляемое слово',
          subtitle: '«и»',
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

/* individual card/item */
.elements__item {
    flex: 0 0 80%;     /* adjust percent for how wide each card should be */
    min-width: 260px;  /* ensures usable width on small screens */
    max-width: 600px;
    scroll-snap-align: center;
    background: transparent;
    box-sizing: border-box;
}

/* keep original wrapper height/spacing inside the horizontal item */
.elements__wrapper {
    height: calc(2/3 * 100vh);
    margin-bottom: 0;
    text-align: left;
    padding: 16px;
    border-radius: 8px;
    /* optional card visuals */
    background: rgba(255,255,255,0.03);
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.elements__title {
    margin: 0;
}

.elements__subtitle {
    margin: 0;
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
