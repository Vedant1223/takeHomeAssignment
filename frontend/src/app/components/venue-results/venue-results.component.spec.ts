import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CommonModule } from '@angular/common';
import { VenueResultsComponent } from './venue-results.component';

describe('VenueResultsComponent', () => {
  let component: VenueResultsComponent;
  let fixture: ComponentFixture<VenueResultsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VenueResultsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VenueResultsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
