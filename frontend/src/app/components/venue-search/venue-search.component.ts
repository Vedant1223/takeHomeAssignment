import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-venue-search',
  imports: [FormsModule, CommonModule],
  templateUrl: './venue-search.component.html',
  styleUrl: './venue-search.component.scss'
})
export class VenueSearchComponent {
  queryText = '';
  
  @Output() searchQuery = new EventEmitter<string>();
  @Output() sqlQuery = new EventEmitter<string>();
  
  search() {
    if (this.queryText.trim()) {
      this.searchQuery.emit(this.queryText);
    }
  }
  
  showSql() {
    if (this.queryText.trim()) {
      this.sqlQuery.emit(this.queryText);
    }
  }
}