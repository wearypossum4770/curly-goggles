import React from "react";
import { render } from "@testing-library/react";
import App from "../App";
import BackEnd from "../components/BackEnd";

const url = "http://127.0.0.1:8000/";

describe("<App/>", () => {
  it("passes if test framework is configured correctly", () =>
    expect(true).toBe(true));
});
