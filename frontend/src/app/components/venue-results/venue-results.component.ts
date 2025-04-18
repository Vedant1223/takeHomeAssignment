import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-venue-results',
  imports: [CommonModule],
  templateUrl: './venue-results.component.html',
  styleUrl: './venue-results.component.scss'
})
export class VenueResultsComponent {
  @Input() venues: any[] = [];
  @Input() error: string | null = null;
}