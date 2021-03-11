import Spell, { SpellDTO } from "@/models/Spell";
import axios from "axios";
import { API_URL } from "@/api/ApiVars";

export abstract class SpellApi {
  private static spellAxios = axios.create();

  static async getAllSpells(): Promise<Spell[]> {
    console.log(`Getting spells from ${API_URL}/spells/`);
    const response = await this.spellAxios.get<SpellDTO[]>(
      `${API_URL}/spells/`
    );

    console.log(response);

    return response.data.map((spellDTO) => new Spell(spellDTO));
  }

  static async getSpell(id: string): Promise<Spell> {
    const response = await this.spellAxios.get<SpellDTO>(
      `${API_URL}/spells/${id}/`
    );
    return new Spell(response.data);
  }

  static async uploadSpellJSON(json: File): Promise<Spell[] | string> {
    const formData = new FormData();
    formData.append("file", json);
    try {
      const response = await this.spellAxios.post<SpellDTO[]>(
        `${API_URL}/spells/`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      return response.data.map((dto) => new Spell(dto));
    } catch {
      return "Failed to insert";
    }
  }
}
