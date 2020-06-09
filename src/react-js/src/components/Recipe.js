import React from 'react';

import { Link } from "react-router-dom";

class Recipe extends React.Component {

  state = {
    activeRecipe: []
  }

  componentDidMount = async () => {
    const { recipe_id } = this.props.match.params
    const req = await fetch(`/api/recipe/${recipe_id}`);

    const res = await req.json();
    console.log(`/api/recipe/${recipe_id} response: `, res)

    this.setState({ activeRecipe: res });
    console.log(this.state.activeRecipe);
  }

  render() {
    const recipe = this.state.activeRecipe;
    return (
      <div className="container">
        { this.state.activeRecipe.length !== 0 &&
          <div className="active-recipe">

            <img className="active-recipe__img" src={recipe.image_url} alt={recipe.title}/>
            <h1><a href={recipe.source_url}>{recipe.title}</a></h1>
            <h4>{recipe.subtitle} </h4>
            <p>Publisher: <a href={recipe.publisher_url}>{recipe.publisher}</a></p>
            <hr/>

            <p>{recipe.description}</p>
            <p><span>{recipe.time}</span> - <span>Serves {recipe.servings}</span></p>
            <hr/>

            <h3>Ingredients:</h3>
            { this.getIngredientsList(recipe) }
            <hr/>

            <h3>Steps:</h3>
            { this.getStepsList(recipe) }
            <hr/>

            { this.getNotesList(recipe) }
            <hr/>

            <button className="active-recipe__button">
              <Link to="/">Go Home</Link>
            </button>
            <p/>

          </div>
        }
      </div>
    );
  }

  getIngredientsList(recipe) {
    console.log("Ingredients: ", recipe.ingredients)

    var ingredients = Object.keys(recipe.ingredients).map(function(ingredient, index) {
      var amount = recipe.ingredients[ingredient]
      return (
        <li key={ingredient}>{amount} {ingredient}</li>
      );
    });
    return <ul>{ingredients}</ul>;
  }

  getStepsList(recipe) {
    // TODO show the images for each step, if available
    var steps = recipe.steps.map(step => {
      return (
        <li>
          <h4>{step.step}</h4>
          <ul>
            {step.steps.map(step => {
              return (<li>{step.step}</li>);
            })}
          </ul>
        </li>
      );
    });
    return <ol>{steps}</ol>
  }

  getNotesList(recipe) {
    return recipe.notes.map(note => {
      return (
        <div><small>{note}</small></div>
      );
    });
  }

};

export default Recipe;