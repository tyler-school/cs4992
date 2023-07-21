//Not sure how this changes with the backend...
import React from 'react';

const ArticleList: React.FC = () => {
  const articles: string[] = ['Article1', 'Article2', 'Article3'];

  return (
    <div>
      <h1>List of Names</h1>
      <ul>
        {articles.map((article, index) => (
          <li key={index}>{article}</li>
        ))}
      </ul>
    </div>
  );
};

export default ArticleList;
