<template>
  <div>
    <div>
      <span class="headline">SpellsJSON</span>
      <span class="font-weight-light headline">Upload</span>
    </div>

    <v-container fill-height>
      <v-row>
        <v-col cols="2"></v-col>
        <v-col cols="8">
          <file-drop v-on:files-selected="uploadSpellsJSON"></file-drop>
        </v-col>
        <v-col cols="2"></v-col>
      </v-row>
    </v-container>
    <v-snackbar v-model="snackbar" :timeout="snackbarTimeout">
      {{ snackbarText }}

      <template v-slot:action="{ attrs }">
        <v-btn color="primary" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Component } from "vue-property-decorator";
import { SpellApi } from "@/api/SpellApi";

// components
import FileDrop from "@/components/FileDrop.vue";

@Component({
  components: {
    FileDrop,
  },
})
export default class App extends Vue {
  snackbar = false;
  snackbarText = "My timeout is set to 2000.";
  snackbarTimeout = 2000;

  snackbarMessage(message: string): void {
    this.snackbarText = message;
    this.snackbar = true;
  }

  uploadSpellsJSON(fileList: FileList): void {
    if (fileList.length > 1) {
      this.snackbarMessage("Only one file can be uploaded");
      return;
    }
    let file = fileList[0];
    if (file.type != "application/json") {
      this.snackbarMessage("JSON file type is required");
      return;
    }
    SpellApi.uploadSpellJSON(file);
  }
}
</script>
