import React, { Component } from "react";
import { Card, Image } from "semantic-ui-react";

class BookDetail extends Component {
  render() {
    const { book } = this.props;
    return (
      <Card>
        <Image src={book.imgUrl} wrapped ui={false} />
        <Card.Content>
          <Card.Header>{book.title}</Card.Header>
          <Card.Meta>
            <div>
              {book.author} &nbsp; {book.publisher}
            </div>
            <div> $ {book.price} </div>
          </Card.Meta>
          <Card.Description>{book.introduce}</Card.Description>
        </Card.Content>
      </Card>
    );
  }
}

export default BookDetail;
