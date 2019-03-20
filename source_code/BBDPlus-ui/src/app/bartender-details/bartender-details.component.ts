import { Component, OnInit } from '@angular/core';
import { BartenderService } from '../bartender.service';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-bartender-details',
  templateUrl: './bartender-details.component.html',
  styleUrls: ['./bartender-details.component.css']
})
export class BartenderDetailsComponent implements OnInit {

  bartenderName: string;
  sales: any[];


  constructor(private bartenderService: BartenderService, private route: ActivatedRoute) {

    route.paramMap.subscribe((paramMap) => {
      
      this.bartenderName = paramMap.get('bartender');
      
      
      bartenderService.shift_sold(this.bartenderName).subscribe(
       data =>{
         this.sales = data;
       },
       (error: HttpResponse<any>) => {
        if (error.status === 404){
          alert('Bartender not found');
        }
        else{
          console.error(error.status + '-' + error.body);
          alert('error occurred on the server. please check the browser console');
        }
      }
      );
    
    
    
    });







   }

  ngOnInit() {
  }

}
