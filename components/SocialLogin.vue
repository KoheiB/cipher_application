<template>
  <v-row justify="center">
    <v-col sm="12">
      <v-btn
        block
        class="color-twitter text-capitalize mb-3"
        @click="twitterLogin"
      >
        <v-icon left class="color-twitter__icon" size="22">
          mdi-twitter
        </v-icon>
        Twitterアカウントでログイン
      </v-btn>
    </v-col>
  </v-row>
</template>

<style lang="scss" scoped>
@mixin social_button($brand-color: #999, $text-color: #fff) {
  background-color: $brand-color !important;
  border-color: $brand-color;
  color: $text-color;

  @at-root {
    #{&}__icon {
      position: absolute;
      left: 0;
    }
  }
}

.color-twitter {
  @include social_button(#1da1f2);
}
.color-facebook {
  @include social_button(#3b5998);
}
.color-google {
  @include social_button(#fff, #757575);
  @at-root {
    #{&}__icon > svg {
      position: absolute;
    }
  }
}
</style>

<script>
export default {
  methods: {
    twitterLogin() {
      this.$store
        .dispatch('signInWithTwitter')
        .then(() => {
          this.$router.push({
            name: 'index',
          })
        })
        .catch((err) => {
          this.$parent.socialLoginErrorMsg =
            '現在Twitterでのログインは使用できません。後ほどお試しください。'
          print(err)
        })
    },
  },
}
</script>
