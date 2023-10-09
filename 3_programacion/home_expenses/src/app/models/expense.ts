import { Category } from './category';

export class Expense {
  constructor(
    public id: string,
    public name: string,
    public detail: string,
    public price: number,
    public category: Category,
    public date: Date,
  ) {}
}
