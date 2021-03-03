import React, { Component } from "react";
import { Grid } from "semantic-ui-react";

import BookList from "./component/BookList";
import BookDetail from "./component/BookDetail";

import Books from "./Books";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      books: Books,
      book: Books[0],
    };
  }

  onBookSelect = (selectbook) => {
    this.setState({
      book: selectbook,
    });
  };

  render() {
    return (
      <Grid columns={2}>
        <Grid.Column>
          <BookList books={this.state.books} bookSelect={this.onBookSelect} />
        </Grid.Column>
        <Grid.Column>
          <BookDetail book={this.state.book} />
        </Grid.Column>
      </Grid>
    );
  }
}

export default App;
