import logo from './logo.svg';
import './App.css';

import TaskListComponent from './components/container/task_list';

import Ejemplo2 from './hooks/Ejemplo2';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Ejemplo2></Ejemplo2>

        </header>
    </div>
  );
}

export default App;
