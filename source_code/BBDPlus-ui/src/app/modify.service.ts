import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


export interface Bar{
  name: string;
  open : string;
  close : string;
  license : string;
  phone : string;
  address : string;
  city : string;
  state : string; 
}



@Injectable({
  providedIn: 'root'
})
export class ModifyService {

  constructor(
    public http: HttpClient
    ) { }


  submitQuery(post: string) {
    const body={q: post}
    return this.http.post<string>('/api/sqlQuery', body);
  }

  getBars() {
    return this.http.get<Bar[]>('/api/bar');
  }

  addBar(name: string, open : string, close : string, license : string, phone : string, address : string, city : string, state : string){
    const body={
      barName: name,
      barOpen : open,
      barClose : close,
      barLicense : license,
      barPhone : phone,
      barAddress : address,
      barCity : city,
      barState : state
    }
    return this.http.post<string>('/api/addBar', body);

  }

  deleteBar(name: string){
    return this.http.get<string>('/api/bar/delete/'+name);
  }


  getBartenders(){
    return this.http.get<any[]>('/api/bartender')
  }


  addBartender(name: string){
    const body={
      bartenderName: name
    }
    return this.http.post<string>('/api/addBartender', body);

  }

  deleteBartender(name: string){
    return this.http.get<string>('/api/bartender/delete/'+name);
  }

  getInventorys(){
    return this.http.get<any[]>('/api/inventory')
  }


  getItems(){
    return this.http.get<any[]>('/api/item')
  }

  getLikes(){
    return this.http.get<any[]>('/api/like')
  }

  getSells(){
    return this.http.get<any[]>('/api/sell')
  }


  getShifts(){
    return this.http.get<any[]>('/api/shift')
  }


  addShift(bar: string, bartender : string, start : string, end : string, date:string){
    const body={
      shiftBar: bar,
      shiftBartender : bartender,
      shiftStart : start,
      shiftEnd : end,
      shiftDate : date
    }
    return this.http.post<string>('/api/addShift', body);

  }

  deleteShift(bar: string, bartender : string, start : string, end : string, date:string){
    const body={
      shiftBar: bar,
      shiftBartender : bartender,
      shiftStart : start,
      shiftEnd : end,
      shiftDate : date
    }
    return this.http.get<string>('/api/shift/delete/'+ body);
  }



  getTransactions(){
    return this.http.get<any[]>('/api/transaction')
  }

  addTransaction(bill: string, item : string, count : string){
    const body={
      transactionBill: bill,
      transactionItem : item,
      transactionCount : count,
    }
    return this.http.post<string>('/api/addTransaction', body);

  }

  deleteTransaction(name: string){
    return this.http.get<string>('/api/transaction/delete/'+ name);
  }


  getBeers(){
    return this.http.get<any[]>('/api/beer')
  }


  addBeer(item: string, manufacturer: string){
    const body={
      itemName: item,
      manufacturerName: manufacturer
    }
    return this.http.post<string>('/api/addBeer', body);

  }

  deleteBeer(item: string){
    return this.http.get<string>('/api/beer/delete/'+item);
  }

  getBills(){
    return this.http.get<any[]>('/api/bill')
  }

  


  getDrinkers(){
    return this.http.get<any[]>('/api/drinker')
  }


  addDrinker(name: string, city: string, state: string, phone: string, address: string){
    const body={
      drinkerName: name,
      cityName: city,
      stateName: state,
      phoneName: phone,
      addressName: address
    }
    return this.http.post<string>('/api/addDrinker', body);

  }

  deleteDrinker(name: string){
    return this.http.get<string>('/api/drinker/delete/'+name);
  }


  getFood(){
    return this.http.get<any[]>('/api/food')
  }



  getFreqs(){
    return this.http.get<any[]>('/api/freqs')
  }

}