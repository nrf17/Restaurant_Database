import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ManufacturerService {

  constructor(private http: HttpClient) { }


  get_manufacturers(){
    return this.http.get<any[]>('/api/manufacturers')
  }


  manuf_high_sales(manuf: string){
    return this.http.get<any[]>('/api/manufacturers/' + manuf)
  }


  manuf_likes(manuf: string){
    return this.http.get<any[]>('/api/manufacturers/' + manuf + '/likes')
  }


}