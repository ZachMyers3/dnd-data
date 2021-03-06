<template>
  <div v-if="!loading">
    <v-card>
      <v-card-title>
        Characters
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="characters"
        :item-key="characters._id"
        :search="search"
        dense
      >
        <!-- templatizes the fullname field, adds router link -->
        <template v-slot:item.fullName="{ item }">
          <div class="fullName">
            <router-link
              :to="{ name: 'characterInfo', params: { id: item._id } }"
            >
              {{ item.fullName }}
            </router-link>
          </div>
        </template>
      </v-data-table>
    </v-card>
  </div>
  <div v-else>
    <v-overlay>
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import Character from "@/models/Character";
import { CharacterApi } from "@/api/CharacterApi";

@Component({})
export default class Characters extends Vue {
  private loading = false;
  private search = "";
  // eslint-disable-next-line
  private headers: any[] = [
    { text: "Name", value: "fullName" },
    { text: "HP", value: "maxHP" },
    { text: "STR", value: "strength" },
    { text: "DEX", value: "dexterity" },
    { text: "CON", value: "constitution" },
    { text: "INT", value: "intelligence" },
    { text: "WIS", value: "wisdom" },
    { text: "CHA", value: "charisma" },
  ];
  // gather characters from API
  private characters: Character[] = [];
  async mounted(): Promise<void> {
    this.getAllCharacters();
  }

  async getAllCharacters(): Promise<void> {
    this.loading = !this.loading;
    this.characters = await CharacterApi.getAllCharacters();
    this.loading = !this.loading;
  }
}
</script>

<style lang="scss">
div.fullName {
  a {
    color: #2c3e50;
    text-decoration: none;
  }
}

div.characterpage {
  h2 {
    text-decoration: underline;
  }
  p.meta {
    font-style: italic;
  }
}
</style>
