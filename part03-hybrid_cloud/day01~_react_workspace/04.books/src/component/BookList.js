import React, { Component } from "react";
import { Item } from "semantic-ui-react";
import BookItem from "./BookItem";

class BookList extends Component {
  render() {
    const { books, bookSelect } = this.book;
    const listItems = books.map((book) => {
      return <BookItem key={book.ISBN} book={book} bookSelect={bookSelect} />;
    });
    return <Item.Group>{listItems}</Item.Group>;
  }
}

export default BookList;
