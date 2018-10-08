import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";

const App = () => (

  <div>
  <DataProvider endpoint="/api/cars/?format=json"
                render={data => <Table data={data} />} />
   <DataProvider endpoint="/api/rentals/?format=json"
                render={data => <Table data={data} />} />
  </div>
);

const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;