import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BartenderService {

  constructor(private http: HttpClient) { }


  getBartenders(){
    return this.http.get<any[]>('/api/bartender')
  }

  shift_sold(name){
    return this.http.get<any[]>('/api/bartender/' + name)
  }

}
