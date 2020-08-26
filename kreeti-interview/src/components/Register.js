import React, { useState } from 'react';
import { navigate } from '@reach/router';

export default function Register() {
    const [state, setState] = useState({
        name: '',
        email: '',
        dob: '',
    });

    const handleChange = (event) => {
        console.log(event.target.name, event.target.value);
        setState({
            ...state,
            [event.target.name]: event.target.value
        });
    }

    const onSubmit = (event) => {
        event.preventDefault();
        console.log(state);
        navigate('/test');
    }
    
    return(
        <div className="w-full">
            <div className="grid grid-cols-6 m-20">
                <div className="col-start-3 col-end-5">
                    <h2 className="text-lg text-bold p-4 text-left">Kreeti Interview</h2>
                    <form>
                        <div className="py-2">
                            <label>Name: </label>
                            <input className="border-solid border-2" name="name" value={state.name} onChange={handleChange} />
                        </div>
                        <div className="py-2">
                            <label>Email: </label>
                            <input className="border-solid border-2" type="email" name="email" value={state.email} onChange={handleChange} />
                        </div>
                        <div className="py-2">
                            <label>DOB: </label>
                            <input className="border-solid border-2" type="date" name="dob" value={state.dob} onChange={handleChange} />
                        </div>
                        <div>
                            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4" type="submit" onClick={onSubmit}>Start Test</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}