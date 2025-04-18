import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface VenueQueryResponse {
  status: string;
  venues?: any[];
  sql_executed?: string;
  message?: string;
}

export interface QueryInput {
  query: string;
}

@Injectable({
  providedIn: 'root'
})
export class VenueService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  // Get venue recommendations based on natural language query
  getVenueRecommendations(query: string): Observable<VenueQueryResponse> {
    return this.http.post<VenueQueryResponse>(`${this.apiUrl}/recommend`, { query });
  }

  // Get SQL query from natural language
  getSqlQuery(query: string): Observable<VenueQueryResponse> {
    return this.http.post<VenueQueryResponse>(`${this.apiUrl}/query`, { query });
  }
}