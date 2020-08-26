import React, { useState, useEffect, useContext } from 'react';
import Question from './Question';
import QuestionMap from './QuestionMap';
import { QuestionsContext } from '../provider/QuestionsContext';

export default function Test() {
    const [state, setState] = useState(useContext(QuestionsContext));
    const [current, setCurrent] = useState(1);
    const [answers, setAnswers] = useState(Array(state.questions.length).fill(null));
    const [visited, setVisited] = useState(Array(state.questions.length).fill(false));
    //const [state, setState] = useState({
    //    current: 1
    //})

    const questionChange = (event, i) => {
        console.log(event.target.value);
        setCurrent(parseInt(event.target.value));
        let newVis = [...visited];
        newVis[event.target.value-1] = true;
        setVisited(newVis);
    }

    const onSaveAnswer = (i, answer) => {
        console.log(i, answer);
        let newAns = [...answers];
        newAns[i-1] = answer;
        setAnswers(newAns);
    }

    useEffect(() => {
        console.log(state);
        console.log(answers);
        console.log(visited);
    }, [state, answers, visited]);

    return(
        <div className="w-full h-100">
            <h2 className="text-lg text-bold p-4 text-left">Kreeti Interview</h2>
            <div className="grid grid-cols-8 gap-2 p-8">
                <div className="col-span-5 w-full">
                    {state.questions.map((question, i) => <div style={{ display: (current === question.id) ? '' : 'none' }}><Question question={question} saveAnswer={onSaveAnswer} answerSaved={answers[i]} /></div>)}
                </div>
                <div className="col-span-3"><QuestionMap questions={state.questions} questionChange={questionChange} answers={answers} visited={visited} /></div>
            </div>
        </div>
    );
}