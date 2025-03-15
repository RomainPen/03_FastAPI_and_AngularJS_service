import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})


export class SearchService {

  private apiUrl = 'http://51.158.116.93:8500'; // URL de votre API FastAPI

  constructor(private http: HttpClient) { }

  /**
   * Recherche de documents par mot-clé
   * @param keyword Le mot-clé à rechercher
   * @returns Observable avec la réponse de l'API
   */
  searchDocuments(keyword: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/searchdocument/${keyword}`);
  }
}
