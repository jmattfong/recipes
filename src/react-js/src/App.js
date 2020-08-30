import React, { Component } from 'react';
import './App.css';

import SearchBar from "./components/SearchBar";
import Recipes from "./components/Recipes";

class App extends Component {
  state = {
    recipes: []
  }

  submitSearchForm = async (e) => {
    const recipeName = e.target.elements.recipeName.value;
    e.preventDefault();

    const data = await this.searchRecipes(recipeName)

    console.log('Search returned: ', data)

    if (data.recipes != null) {
      this.setState({ recipes: data.recipes });
    }
    console.log('State is: ', this.state.recipes);
  }

  searchRecipes = async (recipeName) => {
    const api_call = await fetch(`/api/recipe?q=${recipeName}&limit=12`);
    return await api_call.json();
  }

  suggestRecipes = async () => {
    const api_call = await fetch(`/api/recipe?limit=12`);
    return await api_call.json();
  }

  componentDidMount = () => {
    const json = sessionStorage.getItem("recipes");
    const recipes = JSON.parse(json);
    if (recipes != null) {
      this.setState({ recipes });
    } else {
      this.suggestRecipes().then(data => {
        if (data.recipes != null) {
          this.setState({ recipes: data.recipes });
        }
      });
    }
  }

  componentDidUpdate = () => {
    const recipes = JSON.stringify(this.state.recipes);
    sessionStorage.setItem("recipes", recipes);
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Recipes!</h1>
        </header>
        <SearchBar searchFunction={this.submitSearchForm} />
        <Recipes recipes={this.state.recipes} />
      </div>
    );
  }

}

export default App;
