import React from 'react';
import './App.css';
import './css/index.css';
import Register from './components/Register';
import Test from './components/Test';
import { Router } from '@reach/router';
import { QuestionsContext } from './provider/QuestionsContext';
import QuestionsData from './data/questions.json';
import QuestionMap from './components/QuestionMap';

export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            questions: QuestionsData,
            display: 0,
            answers: Array(QuestionsData.length).fill(null)
        };
        this.saveAnswer = this.saveAnswer.bind(this);
    }

    saveAnswer(i, a) {
        console.log(i, a);
        //this.setState({ ...this.state.answers, answers });
    }

    render() {
        console.log(this.state);
        return (
            <QuestionsContext.Provider value={this.state}>
                <Router>
                    <Register path="/" />
                    <Test path="/test" />
                    <QuestionMap path="/question" />
                </Router>
            </QuestionsContext.Provider>
        );
    }
}

