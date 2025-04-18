import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-sql-display',
  imports: [CommonModule],
  templateUrl: './sql-display.component.html',
  styleUrl: './sql-display.component.scss'
})
export class SqlDisplayComponent {
  @Input() sqlQuery: string | null = null;
  @Input() error: string | null = null;
}