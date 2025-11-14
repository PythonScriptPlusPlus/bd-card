<template>
    <div>
        <h1 class="wishes__title">Пожелания</h1>
        <h2 class="wishes__subtitle">От друзей и близких</h2>
        <div class="wishes">
            <div
                v-for="wish in wishes"
                :key="wish.from"
                class="wishes__wrapper"
                :data-from="wish.from"
            >
                <div v-if="wish.from === 'VASSSSS'">
                  <canvas ref="confettiCanvas" class="wishes__canvas"></canvas>
                  <h3 class="wishes__from">От: {{ wish.from }}</h3>
                  <p class="wishes__message">{{ wish.message }}</p>
                  <component v-if="wish.component" :is="wish.component" />
                </div>
                <div v-else>
                  <h3 class="wishes__from">От: {{ wish.from }}</h3>
                  <p class="wishes__message">{{ wish.message }}</p>
                  <component v-if="wish.component" :is="wish.component" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import confetti from 'canvas-confetti';
import ArishaComponent from './people/ArishaComponent.vue';
import UlyaComponent from './people/UlyaComponent.vue';
import VasComponent from './people/VasComponent.vue';

export default {
  components: {
    ArishaComponent,
    UlyaComponent,
    VasComponent,
  },
  data() {
    return {
      wishes: [
        {
          from: 'Georgie',
          message: 'С днём рождения Алис! 20 лет - это вообще ужас как круто. Цезарь стал сенатором в 20, Beatles выпустили свой первый мега успешный альбом - люди делают невероятные дела когда им 20, и я очень рад, что мне удастся увидеть какие потрясающие достижения ты сделаешь за этот год! А ты их точно сделаешь, потому что когда вообще ты не достигала высот?',
        },
        {
          from: 'VASSSSS',
          message: 'все также без ума от тебя, любимка, как и в нашу первую встречу!!!!! очень скучаю по тебе и надеюсь, что твоя жизнь будет как наш эпик детсадовский утренник🫵🫵 я проверю',
        },
        {
          from: 'Кати крекер',
          message: 'Желаю что бы горизонты возможного были всегда открыты для тебя, что бы твои страхи и обиды остались в прошлом, живи так как указывает тебе сердце ♥️',
        },
        {
          from: 'Полинка (По)',
          message: 'Поздравляю тебя с днем рождения!!!! Ты супер крутая!!! Я очень рада что обстоятельства жизни так сложись и у меня появился пример такого светлого, позитивного и сильного человека как ты!!! Я желаю тебе, чтобы невзгоды обходили тебя стороной, крепкого здоровья, финансового благополучия и побольше путешествий!!!!',
        },
        {
          from: 'уля шутила',
          message: 'желаю фонтаны фанты и реки кока-колы, море хайпа и горы рофла, ну и целый самолёт свега!!!!!',
          component: 'UlyaComponent',
        },
        {
          from: 'Ирина наполеон император завоеватель шкодник',
          message: 'Моя милая Алис, любимая, эти годы, проведенные с тобой - сказка. Ты самый лучший подарок, который мог мне сделать туалет первого мока🙏 я безмерно рада, что могу разделить вместе с тобой этот прекрасный день - день твоего рождения. Считаю, что нужно сделать этот праздник государственным (когда я стану полноправным императором, я обязательно займусь этим вопросом). Прекрасно помню тот день, когда мы говорили до 5 часов утра, это самый яркий пример случая, если никто не скажет «уже пора», полагаю, если бы не потребность в сне, мы бы могли сидеть сутками, ведь мы и есть единая душа, разлитая в разные телесные оболочки, нам суждено было встретиться и это судьбоносное событие произошло! Я очень тебя люблю, надеюсь, наш тандем проживет века и реинкарнирует в новые виды. Ты самая милейшая и прекрасная дама на этом свете, я так тебя люблю что щас умру пока печатаю, боже дудзкпжьвжужкбада, ты моя зажадпоадкдабдпдп🥴🫣🫣🫶🏻😍😍🥴🥴🙏🙏🫶🏻🥵🥵',
        },
        {
          from: 'ариша',
          message: 'алис, очень тебя люблю и всегда рядом! сияй, звездочка!! <3',
          component: 'ArishaComponent',
        },
      ],
      vasObserver: null,
      vasFired: false,
      myConfetti: null,
    };
  },
  mounted() {
    // wait until DOM rendered
    this.$nextTick(() => {
      const el = this.$el.querySelector('.wishes__wrapper[data-from="VASSSSS"]');
      if (!el) return;

      // find the canvas inside the VASSSSS wrapper
      const canvas = el.querySelector('.wishes__canvas');
      if (canvas) {
        this.myConfetti = confetti.create(canvas, { resize: true });
      }

      this.vasObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && !this.vasFired) {
            this.vasFired = true;
            this.fireConfetti();
          }
        });
      }, { threshold: 0.5 });

      this.vasObserver.observe(el);
    });
  },
  beforeUnmount() {
    if (this.vasObserver) {
      this.vasObserver.disconnect();
      this.vasObserver = null;
    }
  },
  methods: {
    fireConfetti() {
      if (!this.myConfetti) return;
      this.myConfetti({
        // angle: 135,
        decay: 0.91,
        gravity: 0.5,
        startVelocity: 33,
        spread: 80,
        particleCount: 150,
        origin: { x: 0.5, y: 1 },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.wishes {
  padding: 20px;

  &__canvas {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 100vw;
    aspect-ratio: 1/2;
    // height: 100%;
    pointer-events: none;
    z-index: 1;
  }

  &__title {
    font-size: 2rem;
    margin-bottom: 0;
  }

  &__subtitle {
    font-size: 1.5rem;
    margin: 0;
  }

  &__wrapper {
    position: relative;
    width: 85%;
    text-align: left;
    padding: 10px;
    margin-bottom: 30px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);

    &:nth-of-type(even) {
      margin-left: calc(15% - 20px);
      text-align: right;
      background-color: #f9f9f9;
    }

    &:nth-of-type(1) {

      &::before {
        border-radius: 8px;
        background-image: url('/public/img/Absolute\ Cinema\ Meme.jpg');
        background-size: cover;
        /* replace $SELECTION_PLACEHOLDER$ with these lines inside the ::before */
        background-repeat: repeat-x;
        background-position: 0 0;
        animation: bg-slide 40s linear infinite;

        /* also add this keyframes block somewhere in the same <style> (outside the selector) */
        @keyframes bg-slide {
          from { background-position: 0 0; }
          to   { background-position: -1000px 0; } /* adjust -1000px or duration to control speed */
        }
        content: "";
        position: absolute;
        top: 0;
        left: 0px;
        width: 100%;
        height: 100%;
        opacity: 0.1;
        z-index: 0;
      }
    }
  }

  &__from {
    font-size: 1.4rem;
    font-weight: bold;
    margin: 0;
  }
  &__message {
    font-size: 1.2rem;
    margin: 0;
  }
}
</style>
