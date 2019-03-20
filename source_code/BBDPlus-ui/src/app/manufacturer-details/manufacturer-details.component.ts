import { Component, OnInit } from '@angular/core';
import { ManufacturerService } from '../manufacturer.service';
import { ActivatedRoute } from '@angular/router';
import { HttpResponse } from '@angular/common/http';



@Component({
  selector: 'app-manufacturer-details',
  templateUrl: './manufacturer-details.component.html',
  styleUrls: ['./manufacturer-details.component.css']
})
export class ManufacturerDetailsComponent implements OnInit {

  manufName: string;
  highSales: any[];
  likesSales: any[];


  constructor(private manufacturerService: ManufacturerService, private route: ActivatedRoute) { 

    route.paramMap.subscribe((paramMap) => {
      this.manufName = paramMap.get('manufacturer');
      
      
      manufacturerService.manuf_high_sales(this.manufName).subscribe(
       data =>{
         this.highSales = data;
       },
       (error: HttpResponse<any>) => {
         if (error.status === 404){
           alert('Manufacturer not found');
         }
         else{
           console.error(error.status + '-' + error.body);
           alert('error occurred on the server. please check the browser console');
         }
       }
      );


      manufacturerService.manuf_likes(this.manufName).subscribe(
        data =>{
          this.likesSales = data;
        }
      );



      });
    }

  ngOnInit() {
  }

}