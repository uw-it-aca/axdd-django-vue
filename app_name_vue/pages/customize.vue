// about.vue

<template>
  <DefaultLayout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #description>
      <p class="p-0 col-md-8 lead">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas eget
        pulvinar est. Sed gravida neque justo, pellentesque finibus velit
        scelerisque eu. Curabitur et dolor luctus, convallis magna at, mollis
        purus. Nunc tincidunt risus quis nisl bibendum volutpat. Praesent ut
        tincidunt ex.
      </p>
    </template>

    <template #content>
      <h2>Directories</h2>
      <div class="row">
        <div class="col-6">
          <h3>Layouts</h3>
          <p>
            The <code>default.vue</code> layout is located in the
            <code>/layouts</code> directory. Start with this component to start
            customizing your application boilerplate (i.e. header and footer).
          </p>
        </div>
        <div class="col-6">
          <h3>Pages</h3>
          <p>
            Page components are located in the <code>/pages</code> directory and
            are mapped to router configuration located in
            <code>/router/index.js</code>.
          </p>
        </div>
        <div class="col-6">
          <h3>Composables</h3>
          <p>
            Composable functions are located in the
            <code>/composables</code> directory. The following example uses the
            <code>mouse.js</code> composable.
          </p>
          <p>
            <strong>EXAMPLE:</strong> Mouse position is at: {{ x }}, {{ y }}
          </p>
        </div>
        <div class="col-6">
          <h3>Utils</h3>
          <p>
            Utility functions are located in the
            <code>/utils</code> directory. The following example uses the
            <code>format.js</code> utility to access the
            <code>formatPhoneNumber()</code> function.
          </p>
          <p>
            <strong>EXAMPLE:</strong> 2065559876 formatted to
            {{ formatPhoneNumber("2065559876") }}
          </p>
        </div>
        <div class="col-6">
          <h3>Stores</h3>
          <p>
            Store functions are located in the <code>/stores</code> directory.
            Stores allow you to share a state across components and pages. The
            following example uses the <code>hello-world.vue</code> component
            which prints a message that originates from the
            <code>hello.js</code> store.
          </p>
          <p>EXAMPLE: <hello-world /></p>
        </div>
      </div>

      <div class="row">
        <div class="col-6 pb-5">
          <h3>Components</h3>
          <p>
            Single-file components in Vue make up the building blocks of all
            applications. These components are located in the
            <code>/components</code>
            directory. The following <code>hello-world.vue</code> file is an
            example of a very simple component.
          </p>
          <hello-world />
        </div>
      </div>

      <h2>Libraries</h2>
      <div class="row">
        <div class="col-6">
          <h3>Solstice Components</h3>
          <p>
            These are published and maintained components intended to be used
            across D&amp;A applications. The following
            <code>&lt;sol-card&gt;</code> component is a standard content
            container.
          </p>

          <axdd-card>
            <template #body>
              <p class="font-weight-lighter">
                Lasdorem ipsum dolor sit amet, consectetur adipiscing elit.
                Maecenas eget pulvinar est. Sed gravida neque justo,
                pellentesque finibus velit scelerisque eu.
              </p>
            </template>
          </axdd-card>
        </div>
        <div class="col-6">
          <h3>Vue3 MQ (Bootstrap5 preset)</h3>
          <div>{{ mq }}</div>
        </div>
      </div>
    </template>
  </DefaultLayout>
</template>

<script>
import DefaultLayout from "@/layouts/default.vue";
import HelloWorld from "@/components/hello-world.vue";

import { useMouse } from "@/composables/mouse";
import { formatPhoneNumber } from "@/utils/format";

export default {
  name: "PagesCustomize",

  components: {
    DefaultLayout,
    HelloWorld,
  },
  inject: ["mq"],
  // setup() is needed for Composition API
  setup() {
    // instantiate composable
    const { x, y } = useMouse();

    // return all imported functions to be used in the component
    return {
      x,
      y,
      formatPhoneNumber,
    };
  },
  data() {
    return {
      pageTitle: "Customizing your app",
    };
  },
  methods: {},
};
</script>
