import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MdButtonModule, MdInputModule, MdCheckboxModule,
  MdProgressBarModule, MdMenuModule, MdIconModule, MdSelectModule,
  MdCardModule, MdSliderModule, MdListModule, MdDialogModule } from '@angular/material';

@NgModule({
  imports: [
    CommonModule,
    MdButtonModule,
    MdInputModule,
    MdCheckboxModule,
    MdProgressBarModule,
    MdMenuModule,
    MdIconModule,
    MdSelectModule,
    MdCardModule,
    MdSliderModule,
    MdListModule,
    MdDialogModule
  ],
  exports: [
    MdButtonModule,
    MdInputModule,
    MdCheckboxModule,
    MdProgressBarModule,
    MdMenuModule,
    MdIconModule,
    MdSelectModule,
    MdCardModule,
    MdSliderModule,
    MdListModule,
    MdDialogModule
  ],
  declarations: []
})
export class MaterialModule { }
