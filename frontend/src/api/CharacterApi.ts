import Character, { CharacterDTO } from "@/models/Character";
import axios from "axios";
import { API_URL } from "@/api/ApiVars";

interface characterSpellInterface {
  ok: boolean;
  data: CharacterDTO;
}

export abstract class CharacterApi {
  private static charactersAxios = axios.create();

  static async getAllCharacters(): Promise<Character[]> {
    const response = await this.charactersAxios.get<Character[]>(
      `${API_URL}/characters`
    );
    return response.data.map((characterDTO) => new Character(characterDTO));
  }

  static async getCharacter(id: string): Promise<Character> {
    const response = await this.charactersAxios.get<Character>(
      `${API_URL}/characters/${id}/`
    );
    return new Character(response.data);
  }

  static async toggleCharacter(id: string, spell_id: number): Promise<boolean> {
    const response = await this.charactersAxios.put<characterSpellInterface>(
      `${API_URL}/character/learn_spell?_id=${id}&spell_id=${spell_id}`
    );
    return response.data.ok;
  }
}
