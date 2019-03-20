import { Component, OnInit } from '@angular/core';
import { ManufacturerService } from '../manufacturer.service';

@Component({
  selector: 'app-manufacturers',
  templateUrl: './manufacturers.component.html',
  styleUrls: ['./manufacturers.component.css']
})
export class ManufacturersComponent implements OnInit {


  manuf: any[];


  constructor(private manufacturerService: ManufacturerService ) {

    this.manufacturerService.get_manufacturers().subscribe(
      data => {
        this.manuf = data;
      },
      error => {
        alert('Could not retrieve the list');
      }

    );



   } //end of constructor








  ngOnInit() {
  }

}