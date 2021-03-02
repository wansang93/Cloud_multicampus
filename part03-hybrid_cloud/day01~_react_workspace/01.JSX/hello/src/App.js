// 1. 함수로 React Component로 부르기
// function App() {
//   return <h1>Hello React!! - Wansang Kim</h1>;
// }

// export default App;

// // export default App;

// 2. 클래스로 React Component로 부르기
import React, { Component} from 'react';

class App extends Component {
  render() {
    return (
      <div>
        <h1>Hello Wansang</h1>
      </div>
    );
  }
}

export default App;
