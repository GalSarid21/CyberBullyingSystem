import {Route, Routes} from 'react-router-dom'

import AlertsPage from './pages/Alerts';
import ReportsPage from './pages/Reports';
import ProjectPage from './pages/Project';
import NlpModelPage from './pages/NlpModel';
import Layout from './components/layouts/Layout';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path='/' element={<ProjectPage />} />
        <Route path='/nlp-model' element={<NlpModelPage />} />
        <Route path='/reports' element={<ReportsPage />} />
        <Route path='/alerts' element={<AlertsPage />} />
      </Routes>
    </Layout>
  );
}

export default App;
