import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SqlDisplayComponent } from './sql-display.component';

describe('SqlDisplayComponent', () => {
  let component: SqlDisplayComponent;
  let fixture: ComponentFixture<SqlDisplayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SqlDisplayComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SqlDisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
