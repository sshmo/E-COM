import React, { Component } from "react";

import axios from "axios";

class App extends Component {
  state = {
    products: [],
  };
  // new
  componentDidMount() {
    this.getProduct();
  }
  // new
  getProduct() {
    axios
      .get("http://127.0.0.1:8000/api/v1/product")
      .then((res) => {
        this.setState({ products: res.data });
      })
      .catch((err) => {
        console.log(err);
      });
  }
  render() {
    return (
      <div>
        {this.state.products.map((item) => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.description}</span>
          </div>
        ))}
      </div>
    );
  }
}
export default App;
