import { Component, OnInit } from '@angular/core';
import { MdDialog, MdDialogRef } from '@angular/material';

import { InviteUserModalComponent } from '../';

@Component({
  selector: 'skael-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss']
})
export class UsersComponent implements OnInit {

  users = [];

  constructor(
    public dialog: MdDialog
  ) { }

  ngOnInit() {
    for (let i = 0; i < 12; i++) {
      this.users.push(i);
    }
  }

  onAddNewUser() {
    const dialogRef = this.dialog.open(InviteUserModalComponent);
    dialogRef.afterClosed().subscribe(result => {
      console.log(result);
    });
  }
}
