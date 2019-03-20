import { Component, OnInit } from '@angular/core';
import {ConfirmationService} from 'primeng/api';
import {ModifyService, Bar/*, Drinker,Frequent,Likes, Beer, Food, SoftDrink*/} from '../modify.service';
@Component({
  selector: 'app-modify',
  templateUrl: './modify.component.html',
  styleUrls: ['./modify.component.css'],
  providers: [ConfirmationService]
})
export class ModifyComponent implements OnInit {
  queryReturn: string;
  bars: Bar[];
  bartenders: any[];
  shifts: any[];
  transactions: any[];
  likes:any[];
  sells:any[];
  items:any[];
  inventorys:any[];
  beers: any[];
  bills: any[];
  drinkers: any[];
  foods: any[];
  frequents: any[];
 
  constructor(
    private modifyService: ModifyService,
    private confirmationService: ConfirmationService 
  ) { 
    this.modifyService.getBars().subscribe(
      data => {
        this.bars = data;
      },
      error => {
        console.log('Could not retrieve a list of bars');
      }
    );


    this.modifyService.getBartenders().subscribe(
      data => {
        this.bartenders = data;
      }
    ); 


    this.modifyService.getBeers().subscribe(
      data => {
        this.beers = data;
      }
    ); 

    this.modifyService.getBills().subscribe(
      data => {
        this.bills = data;
      }
    ); 


    this.modifyService.getDrinkers().subscribe(
      data => {
        this.drinkers = data;
      }
    ); 


    this.modifyService.getFood().subscribe(
      data => {
        this.foods = data;
      }
    );


    this.modifyService.getFreqs().subscribe(
      data => {
        this.frequents = data;
      }
    ); 

    this.modifyService.getInventorys().subscribe(
      data => {
        this.inventorys = data;
      }
    ); 


    this.modifyService.getItems().subscribe(
      data => {
        this.items = data;
      }
    ); 

    this.modifyService.getLikes().subscribe(
      data => {
        this.likes = data;
      }
    ); 

    this.modifyService.getSells().subscribe(
      data => {
        this.sells = data;
      }
    ); 

    this.modifyService.getShifts().subscribe(
      data => {
        this.shifts = data;
      }
    ); 

    this.modifyService.getTransactions().subscribe(
      data => {
        this.transactions = data;
      }
    ); 

  }

  ngOnInit() {
  }

  submitQuery(){
    var sqlString=(document.getElementById("sqlquery") as HTMLInputElement).value;

    this.modifyService.submitQuery(sqlString).subscribe(
      data=>{
        this.queryReturn=data;
      },
       error => {
        alert('Could not execute query');
      }

    )
  }
  


  insertBarEvent(event){
    let barName:string=(document.getElementById("bars-barName") as HTMLInputElement).value;
    let barOpen:string=(document.getElementById("bars-barOpen") as HTMLInputElement).value;
    let barClose:string=(document.getElementById("bars-barClose") as HTMLInputElement).value;
    let barLicense:string=(document.getElementById("bars-barLicense") as HTMLInputElement).value;
    let barPhone:string=(document.getElementById("bars-barPhone") as HTMLInputElement).value;
    let barAddress:string=(document.getElementById("bars-barAddress") as HTMLInputElement).value;
    let barCity:string=(document.getElementById("bars-barCity") as HTMLInputElement).value;
    let barState:string=(document.getElementById("bars-barState") as HTMLInputElement).value;
    this.modifyService.addBar(barName, barOpen, barClose, barLicense, barPhone, barAddress, barCity, barState).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not add bar');
      }
      
    );
  }


  
  deleteBarClick(event){
    let barDelete:string=(document.getElementById("bars-barDelete") as HTMLInputElement).value;
    this.modifyService.deleteBar(barDelete).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not delete bar');
      }
      
    );

  }

  
  insertBartenderEvent(event){
    let bartenderName:string=(document.getElementById("bartender-bartenderName") as HTMLInputElement).value;
    this.modifyService.addBartender(bartenderName).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not add bartender');
      }
      
    );
  }


  
  deleteBartenderClick(event){
    let bartenderDelete:string=(document.getElementById("bartender-bartenderDelete") as HTMLInputElement).value;
    this.modifyService.deleteBartender(bartenderDelete).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not delete bartender');
      }
      
    );

  }
  

  insertTransactionEvent(event){
    let transactionBill:string=(document.getElementById("transactions-transactionBill") as HTMLInputElement).value;
    let transactionItem:string=(document.getElementById("transactions-transactionItem") as HTMLInputElement).value;
    let transactionCount:string=(document.getElementById("transactions-transactionCount") as HTMLInputElement).value;

    this.modifyService.addTransaction(transactionBill, transactionItem, transactionCount).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not add Transaction because of Foreign key');
      }
      
    );
  }
  

  deleteTransactionClick(event){
    let transactionDelete:string=(document.getElementById("transaction-transactionDelete") as HTMLInputElement).value;
    this.modifyService.deleteTransaction(transactionDelete).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not delete transaction');
      }
      
    );

  }

  insertShiftEvent(event){
    let Bar:string=(document.getElementById("shifts-shiftBar") as HTMLInputElement).value;
    let Bartender:string=(document.getElementById("shifts-shiftBartender") as HTMLInputElement).value;
    let Start:string=(document.getElementById("shifts-shiftStart") as HTMLInputElement).value;
    let End:string=(document.getElementById("shifts-shiftEnd") as HTMLInputElement).value;
    let shiftDate:string=(document.getElementById("shifts-shiftDate") as HTMLInputElement).value;
    this.modifyService.addShift(Bar, Bartender, Start,End, shiftDate).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not add Shift because of Foreign key');
      }
      
    );
  }
  

  insertBeerEvent(event){
    let itemName:string=(document.getElementById("beer-beerName") as HTMLInputElement).value;
    let manufacturerName:string=(document.getElementById("beer-manufacturerName") as HTMLInputElement).value;
    this.modifyService.addBeer(itemName, manufacturerName).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not add beer because of foreign key');
      }
      
    );
  }


  
  deleteBeerClick(event){
    let beerDelete:string=(document.getElementById("beer-beerDelete") as HTMLInputElement).value;
    this.modifyService.deleteBeer(beerDelete).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not delete beer');
      }
      
    );
  }
  





   insertDrinkerEvent(event){
    let drinkerName:string=(document.getElementById("drinker-drinkerName") as HTMLInputElement).value;
    let cityName:string=(document.getElementById("drinker-cityName") as HTMLInputElement).value;
    let stateName:string=(document.getElementById("drinker-stateName") as HTMLInputElement).value;
    let phoneName:string=(document.getElementById("drinker-phoneName") as HTMLInputElement).value;
    let addressName:string=(document.getElementById("drinker-addressName") as HTMLInputElement).value;
    this.modifyService.addDrinker(drinkerName, cityName, stateName, phoneName, addressName).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not add drinker because of foreign key');
      }
      
    );
  }

  deleteDrinkerClick(event){
    let drinkerDelete:string=(document.getElementById("drinker-drinkerDelete") as HTMLInputElement).value;
    this.modifyService.deleteDrinker(drinkerDelete).subscribe(
      data=>{
        alert(data)
        window.location.reload();

      },
       error => {
        alert('Could not delete Drinker');
      }
      
    );
  }



  // deleteShiftClick(event){
  //   let barDelete:string=(document.getElementById("transaction-transactionDelete") as HTMLInputElement).value;
  //   let bartenderDelete:string=(document.getElementById("transaction-transactionDelete") as HTMLInputElement).value;
  //   let startDelete:string=(document.getElementById("transaction-transactionDelete") as HTMLInputElement).value;
  //   let endDelete:string=(document.getElementById("transaction-transactionDelete") as HTMLInputElement).value;
  //   let dateDelete:string=(document.getElementById("transaction-transactionDelete") as HTMLInputElement).value;

  //   this.modifyService.deleteShift(transactionDelete).subscribe(
  //     data=>{
  //       alert(data)
  //       window.location.reload();

  //     },
  //      error => {
  //       alert('Could not delete Shift');
  //     }
      
  //   );

  // }




}
