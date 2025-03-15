import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { SearchService } from '../../services/search.service';

@Component({
  selector: 'app-search-bar',
  imports: [CommonModule, FormsModule],
  standalone: true,
  templateUrl: './search-bar.component.html',
  styleUrl: './search-bar.component.scss'
})


export class SearchBarComponent {
  searchtitle: string = "Opensearch project";
  searchTerm: string = '';
  searchResult: any = null;
  isLoading: boolean = false;
  hasError: boolean = false;
  errorMessage: string = '';

  constructor(private searchService: SearchService) {}

  onSearch(): void {
    if (this.searchTerm.trim()) {
      this.isLoading = true;
      this.hasError = false;
      this.searchResult = null;

      this.searchService.searchDocuments(this.searchTerm)
        .subscribe({
          next: (response) => {
            this.searchResult = response;
            this.isLoading = false;
            console.log('Résultat de la recherche:', response);
          },
          error: (error) => {
            this.isLoading = false;
            this.hasError = true;
            this.errorMessage = error.API_message || 'Une erreur est survenue lors de la recherche';
            console.error('Erreur de recherche:', error);
          }
        });
    }
  }
}
