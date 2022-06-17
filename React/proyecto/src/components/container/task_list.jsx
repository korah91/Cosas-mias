import React from 'react';
import { Task } from '../../models/task.class'
import {LEVELS} from '../../models/levels.enum'
import TaskComponent from '../pure/task'

const TaskListComponent = () => {

    const defaultTask = new Task('example', 'default_description', false, LEVELS.NORMAL);



    return (
        <div>
            <div>
                Your Tasks: 
            </div>
            {/*Aplicar un For/Map para renderizar una lista */}
            <TaskComponent task={defaultTask}></TaskComponent>
            
        </div>
    );
};


export default TaskListComponent;
