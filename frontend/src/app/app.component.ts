import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { VenueSearchComponent } from './components/venue-search/venue-search.component';
import { VenueResultsComponent } from './components/venue-results/venue-results.component';
import { SqlDisplayComponent } from './components/sql-display/sql-display.component';
import { VenueService } from './services/venue.service';


@Component({
  selector: 'app-root',
  imports: [RouterOutlet, CommonModule,
    HttpClientModule,
    VenueSearchComponent,
    VenueResultsComponent,
    SqlDisplayComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'frontend';
  venues: any[] = [];
  sqlQuery: string | null = null;
  error: string | null = null;
  showSqlView = false;
  
  constructor(private venueService: VenueService) {}
  
  onSearch(query: string) {
    this.resetState();
    this.showSqlView = false;
    
    this.venueService.getVenueRecommendations(query).subscribe({
      next: (response) => {
        if (response.status === 'success' && response.venues) {
          this.venues = response.venues;
        } else if (response.message) {
          this.error = response.message;
        }
      },
      error: (err) => {
        this.error = 'Error connecting to server. Please try again later.';
        console.error('API error:', err);
      }
    });
  }
  
  onShowSql(query: string) {
    this.resetState();
    this.showSqlView = true;
    
    this.venueService.getSqlQuery(query).subscribe({
      next: (response) => {
        if (response.status === 'success' && response.sql_executed) {
          this.sqlQuery = response.sql_executed;
        } else if (response.message) {
          this.error = response.message;
        }
      },
      error: (err) => {
        this.error = 'Error connecting to server. Please try again later.';
        console.error('API error:', err);
      }
    });
  }
  
  private resetState() {
    this.venues = [];
    this.sqlQuery = null;
    this.error = null;
  }
}