<!-- an image carousel that can show multiple pictures and rotate over them or shows a single picture -->
<!-- TODO continous only works when clicking not on cycle -->
<template>
  <v-carousel
    :height="height"
    :cycle="cycle"
    :interval="cycleInterval"
    :show-arrows="showArrow"
    :show-arrows-on-hover="showArrowsOnHover"
    :hide-delimiters="hideDelimiters"
    hide-delimiter-background
    continuous
  >
    <!-- loop over every image provided by the images prop -->
    <!-- TODO images have no ID -->
    <v-carousel-item
      v-for="image in images"
      :key="image.id"
      :src="image.src"
    >
    </v-carousel-item>
  </v-carousel>
</template>

<script>

export default {
  name: "ImageCarousel",
  props: {
    //array of images ([path, path, ..])
    images: {
      type: Array,
      required: true,
    },
    //hight of the carousel image (size in px)
    height: {
      type: Number,
      required: false,
      default: 300,
    },
    //should the carousel rotate automatically
    cycle: {
      type: Boolean,
      required: false,
      default: false,
    },
     //interval of the rotation, when cycle=true (in ms)
    cycleInterval: {
      type: Number,
      required: false,
      default: 8000,
    },
  },
  // TODO: change to computed props
  data: () => ({
    showArrow: null,
    showArrowsOnHover: null,
    hideDelimiters: null,
  }),
  // if the carousel contains more than one image the carousel arrows
  // are shown on hover and the delimiters are shown
  // otherwise no delimiters or arrows are shown
  created: function() {
    if (this.images.length > 1) {
      this.showArrow = true
      this.showArrowsOnHover = true
      this.hideDelimiters = false
    }
    else {
      this.showArrow = false
      this.showArrowsOnHover = false
      this.hideDelimiters = true
    }
  },
}
</script>
